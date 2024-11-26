import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Index from './pages/Index';
import Marcas from './pages/marcasdeveiculos.jsx';
import Modelos from './pages/modelosdeveiculos.jsx';
import Menu from './components/Menu'
import Footer from './components/Footer'

function App() {
  return (
    <div>
    <Menu></Menu>
      <Router>
        <div>
          <Routes>
            <Route path="/" element={<Index />} />
            <Route path="/marcas" element={<Marcas />} />
            <Route path="/modelos" element={<Modelos />} />
          </Routes>
        </div>
      </Router>
    <Footer></Footer>
    </div>
  );
}

export default App;