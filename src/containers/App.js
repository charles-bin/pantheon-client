import React, { Component } from 'react';
import { connect } from 'react-redux'
import logo from './logo.svg';
import './App.css';
import {
  fetchItems,
  updateItem
} from '../actions'
import { Grid, Row, Col } from 'react-bootstrap'
import CustomNavbar from '../components/CustomNavbar'
import Ranking from '../components/Ranking'

class App extends Component {

  componentDidMount() {
    this.props.dispatch(updateItem())
    this.props.dispatch(fetchItems())
  }

  render() {
    const {
      isFetching,
      items,
    } = this.props

    return (
      <div className="App">
        <CustomNavbar/>
        <Grid fluid>
          <Col
            xs={10} xsOffset={1}
            sm={10} smOffset={1}
            md={10} mdOffset={1}
            lg={10} lgOffset={1}>
            <Ranking items={ items }/>
          </Col>
        </Grid>
      </div>
    );
  }
}

function mapStateToProps(state) {
  const {
    rankings,
  } = state

  // Bind items to the window object for debugging
  window.i1 = rankings.items

  return {
    isFetching: rankings.isFetching,
    items: rankings.items,
  }
}

export default connect(mapStateToProps)(App)
