import React from 'react';
import { NavLink } from 'react-router-dom';
import './Sidebar.css';

const Sidebar = () => {
  return (
    <nav className="sidebar">
      <div className="sidebar-header">
        <h2>NichePulse</h2>
      </div>
      <ul className="sidebar-menu">
        <li>
          <NavLink to="/" className={({ isActive }) => (isActive ? "menu-item active" : "menu-item")}>
            Dashboard
          </NavLink>
        </li>
        <li>
          <NavLink to="/influencers" className={({ isActive }) => (isActive ? "menu-item active" : "menu-item")}>
            Influencers
          </NavLink>
        </li>
        <li>
          <NavLink to="/settings" className={({ isActive }) => (isActive ? "menu-item active" : "menu-item")}>
            Settings
          </NavLink>
        </li>
      </ul>
    </nav>
  );
};

export default Sidebar;