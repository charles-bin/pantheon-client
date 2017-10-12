import React from 'react'
import PropTypes from 'prop-types'
import { ListGroupItem, Image, Row, Col } from 'react-bootstrap'

const centerChildren = {
  display: "flex",
  alignItems: "center",
}

export default function RankingItem(props) {
  const { index, item } = props
  return (
    <li
      className="list-group-item"
      onClick={() => {}}>
      <Row style={centerChildren}>
        <Col
          xs={3} xsOffset={0}
          sm={3} smOffset={0}
          md={3} mdOffset={0}
          lg={3} lgOffset={0}>
          <Image alt={item.title} src={item.image} responsive />
        </Col>
        <Col
          xs={9} xsOffset={0}
          sm={9} smOffset={0}
          md={9} mdOffset={0}
          lg={9} lgOffset={0}>
          <h4>{item.title}</h4>
          <p>{item.developer} - {item.genre}</p>
          <p>{item.description}</p>
        </Col>
      </Row>
    </li>
  )
}

RankingItem.propTypes = {
  index: PropTypes.number.isRequired,
  item: PropTypes.object.isRequired,
}

RankingItem.defaultProps = {
  items: {},
}
