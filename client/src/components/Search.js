import React from 'react'
import { FormGroup, FormControl, HelpBlock } from 'react-bootstrap'

/* Object destructuring notation matches on id, label while type, placeholder
  are keys of the props object. The help variable is currently left undefined.
*/
export default function Search({ id, label, ...props }) {
  return (
    <FormGroup
      controlId={id}
    >
      <FormControl {...props} />
      <FormControl.Feedback />
    </FormGroup>
  )
}
