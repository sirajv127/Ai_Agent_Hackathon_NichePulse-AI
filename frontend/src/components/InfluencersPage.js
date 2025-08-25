import React from 'react';
import AddInfluencerForm from './AddInfluencerForm';
import './Page.css';

const InfluencersPage = () => {
  return (
    <div className="page">
      <header className="page-header">
        <h1>Manage Influencers</h1>
        <p>Add or remove profiles from your tracking list.</p>
      </header>
      <div className="page-content">
        <AddInfluencerForm />
        {/* In the future, a list of current influencers would go here */}
      </div>
    </div>
  );
};

export default InfluencersPage;