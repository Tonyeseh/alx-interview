#!/usr/bin/node

const request = require('request')

resp = request('https://swapi-api.alx-tools.com/api/films/1', function (error, response, body) {
    console.error('error:', error)
    console.log('response:', response)
    console.log('body:', body)
})
