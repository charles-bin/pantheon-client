import { combineReducers } from 'redux'
import {
  REQUEST_ITEMS,
  RECEIVE_ITEMS,
} from './actions'

const defaultState = {
  items: []
}

function rankings(state=defaultState, action) {
  switch (action.type) {
    case REQUEST_ITEMS:
      return {
        ...state,
        isFetching: true
      }
    case RECEIVE_ITEMS:
      return {
        ...state,
        items: action.items,
        isFetching: false
      }
    default:
      return state
  }
}

const rootReducer = combineReducers({
  rankings,
})

export default rootReducer
