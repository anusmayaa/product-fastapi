import React from 'react';
import './TaglineSection.css';

const TaglineSection = () => {
  return (
    <div className="tagline-card">
      <div className="tagline-content">
        <h3>🚀 Simplify. Organize. Succeed.</h3>
        <p>Your all-in-one solution for effortless inventory management and product tracking.</p>
        <div className="feature-pills">
          <span className="pill">⚡ Fast</span>
          <span className="pill">🔒 Secure</span>
          <span className="pill">🎯 Reliable</span>
        </div>
      </div>
    </div>
  );
};

export default TaglineSection;
