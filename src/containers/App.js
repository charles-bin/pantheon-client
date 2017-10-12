import React, { Component } from 'react';
import { connect } from 'react-redux'
import logo from './logo.svg';
import './App.css';
import {
  fetchItems,
  updateItem
} from '../actions'
import { Grid, Row, Col } from 'react-bootstrap'
import Ranking from '../components/Ranking'
import Search from '../components/Search'

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
        <Grid fluid>
          <header className="App-header">
            <img src={logo} className="App-logo" alt="logo" />
            <h1 className="App-title">Pantheon</h1>
          </header>
          <Col style={{paddingBottom: "20px"}}
            xs={6} xsOffset={3}
            sm={6} smOffset={3}
            md={6} mdOffset={3}
            lg={6} lgOffset={3}>
            <Search />
          </Col>
          <Col
            xs={8} xsOffset={2}
            sm={8} smOffset={2}
            md={8} mdOffset={2}
            lg={8} lgOffset={2}>
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
