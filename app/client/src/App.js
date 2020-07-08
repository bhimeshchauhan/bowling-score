import React from 'react';
import './App.css';
import { ManualScore, AutoScore } from './pages/index';

function App() {
  return (
    <div className="App">
      <ManualScore />
      <AutoScore />
    </div>
  );
}

export default App;
