import React from 'react'
import PropTypes from 'prop-types'
import { ListGroup } from 'react-bootstrap'
import RankingItem from './RankingItem'

export default function Ranking(props) {
  const { items } = props
  return (
    <ListGroup componentClass="ul">
      { items.map((m, i) => {
        return (
          <RankingItem index={i} item={m} />
        )
      })}
    </ListGroup>
  )
}

Ranking.propTypes = {
  items: PropTypes.array.isRequired,
}

Ranking.defaultProps = {
  items: [],
}
