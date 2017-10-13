import React from 'react'
import PropTypes from 'prop-types'
import { Image, Glyphicon, Row, Col } from 'react-bootstrap'

const centerChildren = {
  display: "flex",
  alignItems: "center",
}

const voteStyle = {
  textAlign: "center",
  fontSize: "18px"
}

const glyphStyle = {
  cursor: "pointer",
  top: "3px",
  left: "0.4px"
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
          xs={8} xsOffset={0}
          sm={8} smOffset={0}
          md={8} mdOffset={0}
          lg={8} lgOffset={0}>
          <h4>{item.rank} - {item.title}</h4>
          <p>{item.developer} - {item.genre}</p>
          <p>{item.description}</p>
        </Col>
        <Col
          xs={1} xsOffset={0}
          sm={1} smOffset={0}
          md={1} mdOffset={0}
          lg={1} lgOffset={0}>
          <div style={voteStyle}>
            <Glyphicon glyph="chevron-up" style={glyphStyle} />
            <div>0</div>
            <Glyphicon glyph="chevron-down" style={glyphStyle} />
          </div>
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
