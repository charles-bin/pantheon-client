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
          xs={2} xsOffset={0}
          sm={2} smOffset={0}
          md={2} mdOffset={0}
          lg={2} lgOffset={0}>
          <Image alt={item.title} src={item.image} responsive />
        </Col>
        <Col
          xs={9} xsOffset={0}
          sm={9} smOffset={0}
          md={9} mdOffset={0}
          lg={9} lgOffset={0}>
          <h3 style={{fontWeight: "400"}}>{item.rank} - {item.title}</h3>
          <p>{item.developer} - {item.genre}</p>
          <p>Release Date: {item.published}</p>
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
