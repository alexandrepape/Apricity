import axios from 'axios'

let baseURL

if (!process.env.NODE_ENV || process.env.NODE_ENV === 'development') {
  baseURL = 'http://localhost:5000/'
} else {
  baseURL = 'https://api-apricity.herokuapp.com/'
}

export const HTTP = axios.create(
  {
    baseURL: baseURL
  })
