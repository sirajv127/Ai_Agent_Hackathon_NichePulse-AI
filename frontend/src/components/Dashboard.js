import React, { useState, useEffect } from 'react';
import ReportCard from './ReportCard';
import apiClient from '../api/apiClient';
import './Dashboard.css';

const Dashboard = () => {
  const [reports, setReports] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [isGenerating, setIsGenerating] = useState(false);

  // Fetch all stored reports when the component first loads
  useEffect(() => {
    const fetchReports = async () => {
      try {
        setLoading(true);
        const response = await apiClient.get('/reports/');
        setReports(response.data);
        setError(null);
      } catch (err) {
        setError('Failed to fetch initial reports. The backend might be starting up.');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };
    fetchReports();
  }, []);

  // Function to handle the generate button click
  const handleGenerateReport = async () => {
    setIsGenerating(true);
    setError(null);
    try {
      const response = await apiClient.post('/reports/generate');
      setReports(prevReports => [response.data, ...prevReports]);
    } catch (err) {
      setError('Failed to generate new report. Please check the backend logs and your API key.');
      console.error(err);
    } finally {
      setIsGenerating(false);
    }
  };

  // NEW function to handle the delete button click
  const handleDeleteReport = async (reportId) => {
    try {
      // Call the new DELETE endpoint on the backend
      await apiClient.delete(`/reports/${reportId}`);
      // Remove the report from the list in the UI without a page refresh
      setReports(prevReports => prevReports.filter(report => report.id !== reportId));
    } catch (err) {
      setError('Failed to delete report. Please try again.');
      console.error(err);
    }
  };

  return (
    <div className="dashboard">
      <header className="dashboard-header">
        <h1>Dashboard</h1>
        <p>Your trend briefings and historical data.</p>
      </header>
      
      <div className="actions-bar">
        <button 
          className="generate-button" 
          onClick={handleGenerateReport} 
          disabled={isGenerating}
        >
          {isGenerating ? 'Generating with AI...' : 'Track with AI & Generate New Report'}
        </button>
      </div>

      <h2>Stored Reports</h2>
      {loading && <p>Loading reports...</p>}
      {error && <p className="error-message">{error}</p>}
      
      <div className="reports-grid">
        {!loading && reports.length > 0 ? (
          reports.map(report => (
            <ReportCard key={report.id} report={report} onDelete={handleDeleteReport} />
          ))
        ) : (
          !loading && <p>No reports found. Click the button above to generate your first one!</p>
        )}
      </div>
    </div>
  );
};

export default Dashboard;