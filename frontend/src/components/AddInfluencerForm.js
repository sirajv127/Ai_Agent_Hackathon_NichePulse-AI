import React, { useState } from 'react';
import apiClient from '../api/apiClient';
import './AddInfluencerForm.css';

const AddInfluencerForm = () => {
  const [handle, setHandle] = useState('');
  const [platform, setPlatform] = useState('Instagram');
  const [submitting, setSubmitting] = useState(false);
  const [message, setMessage] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!handle) {
      setMessage('Please enter a handle or URL.');
      return;
    }

    setSubmitting(true);
    setMessage('');

    try {
      const response = await apiClient.post('/influencers/', {
        handle: handle,
        platform: platform,
      });
      setMessage(`Successfully added ${response.data.handle}!`);
      setHandle(''); // Clear the form
    } catch (error) {
      setMessage('Failed to add influencer. Please try again.');
      console.error('Submission error:', error);
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <div className="add-influencer-card">
      <h3>Track a New Profile</h3>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="platform">Platform</label>
          <select 
            id="platform" 
            value={platform} 
            onChange={(e) => setPlatform(e.target.value)}
          >
            <option>Instagram</option>
            <option>YouTube</option>
            <option>LinkedIn</option>
          </select>
        </div>
        <div className="form-group">
          <label htmlFor="handle">Profile Handle or URL</label>
          <input
            id="handle"
            type="text"
            value={handle}
            onChange={(e) => setHandle(e.target.value)}
            placeholder="@profilename or youtube.com/..."
          />
        </div>
        <button type="submit" className="primary" disabled={submitting}>
          {submitting ? 'Adding...' : 'Add Profile'}
        </button>
      </form>
      {message && <p className="form-message">{message}</p>}
    </div>
  );
};

export default AddInfluencerForm;