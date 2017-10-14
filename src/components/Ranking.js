import React from 'react'
import PropTypes from 'prop-types'
import { Panel, ListGroup } from 'react-bootstrap'
import RankingItem from './RankingItem'

const panelStyle = {
  boxShadow: "0 0 8px -3px #888888"
}

export default function Ranking(props) {
  const { items } = props
  return (
    <Panel style={panelStyle}>
      <ListGroup componentClass="ul" fill>
        { items.map((m, i) => {
          return (
            <RankingItem index={i} item={m} />
          )
        })}
      </ListGroup>
    </Panel>
  )
}

Ranking.propTypes = {
  items: PropTypes.array.isRequired,
}

Ranking.defaultProps = {
  items: [],
}
