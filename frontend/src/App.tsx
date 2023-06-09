import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './App.css';
import Articles from './pages/articles';

function App() {
  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path="/" element={<Articles />} />
          {/* Add more routes for other pages here */}
        </Routes>
      </Router>
    </div>
  );
}

export default App;
