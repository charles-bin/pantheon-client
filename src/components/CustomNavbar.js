import React from 'react'
import {
  Navbar,
  Nav,
  NavDropdown,
  MenuItem,
  FormGroup,
  FormControl,
} from 'react-bootstrap'

export default function CustomNavbar({ id, label, ...props }) {
  return (
    <Navbar staticTop>
      <Navbar.Header>
        <Navbar.Brand>
          <a href="#">Pantheon</a>
        </Navbar.Brand>
      </Navbar.Header>
      <Navbar.Collapse>
        <Nav>
          <NavDropdown eventKey={1} title="Lists" id="basic-nav-dropdown">
            <MenuItem eventKey={1.1}>Action</MenuItem>
            <MenuItem eventKey={1.2}>Another action</MenuItem>
            <MenuItem eventKey={1.3}>Something else here</MenuItem>
            <MenuItem divider />
            <MenuItem eventKey={1.4}>Separated link</MenuItem>
          </NavDropdown>
        </Nav>
        <Nav pullRight>
          <NavDropdown eventKey={2} title="Account" id="basic-nav-dropdown">
            <MenuItem eventKey={2.1}>Action</MenuItem>
            <MenuItem eventKey={2.2}>Another action</MenuItem>
            <MenuItem eventKey={2.3}>Something else here</MenuItem>
            <MenuItem divider />
            <MenuItem eventKey={2.4}>Separated link</MenuItem>
          </NavDropdown>
        </Nav>
        <Navbar.Form pullRight>
          <FormGroup>
            <FormControl type="text" placeholder="Search" />
          </FormGroup>
        </Navbar.Form>
      </Navbar.Collapse>
    </Navbar>
  )
}
