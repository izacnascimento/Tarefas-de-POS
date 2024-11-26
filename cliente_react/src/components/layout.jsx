import Container from 'react-bootstrap/Container';
import Navbar from 'react-bootstrap/Navbar';


function base() {
  return (
    <Navbar expand="lg" bg="dark" data-bs-theme="dark" fixed="bottom">
      <Container className="d-flex justify-content-center">
        <Navbar.Text className="text-white"></Navbar.Text>
      </Container>
    </Navbar>
  );
}


export default base;