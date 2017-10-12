export const REQUEST_ITEMS = 'REQUEST_ITEMS'
export const RECEIVE_ITEMS = 'RECEIVE_ITEMS'

function requestItems() {
  return {
    type: REQUEST_ITEMS
  }
}

function receiveItems(json) {
  return {
    type: RECEIVE_ITEMS,
    items: json
  }
}

export function fetchItems() {
  return dispatch => {
    dispatch(requestItems())
    return fetch('https://pantheon-server.herokuapp.com/games/')
      .then(response => response.json())
      .then(json => {
        dispatch(receiveItems(json))
      })
      .catch(error => console.log(error))
  }
}

let data = {
  id: 1,
  title: 'foo',
  body: 'bar',
  userId: 1
}

let init = {
  method: 'POST',
  body: data,
  headers: new Headers()
}

export function updateItem() {
  return dispatch => {
    fetch('https://jsonplaceholder.typicode.com/posts/', init)
      .then(data => {
        window.r1 = data
      })
  }
}
