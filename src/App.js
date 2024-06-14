import logo from './logo.svg';
import './App.css';
import { BrowserRouter } from 'react-router-dom';
import { Route } from 'react-router-dom';
import { Routes } from 'react-router-dom';
import Predict from './components/Predict';
import History from './components/History';
import Points from './components/Points';
import Main from './components/Main';
import Worldcup from './components/Worldcup';
import Llm from './components/Llm';
import Profiles from './components/Profiles';
function App() {
  return (
    <BrowserRouter>
    <Routes>
      <Route exact path='/' element={<Main/>}></Route>
      <Route exact path='/Llm' element={<Llm/>}></Route>
      <Route exact path='/Profiles' element={<Profiles/>}></Route>
      <Route exact path='/Worldcup' element={<Worldcup/>}></Route>
      <Route exact path='/Predict' element={<Predict/>}></Route>
      <Route exact path='/History' element={<History/>}></Route>
      <Route exact path='/Points' element={<Points/>}></Route>
      </Routes></BrowserRouter>
  );
}

export default App;
