#!/usr/bin/node

const request = require('request');
const argv = process.argv;

const route = 'https://swapi-api.alx-tools.com/api/films/';

resp = request(`${route}${argv[2]}`, function (error, response, body) {
  if (!error) {
    const data = JSON.parse(body);
    const characters = data.characters;
    printCharacterName(characters, 0);
  }
});

function printCharacterName(characters, idx) {
  request.get(characters[idx], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (idx + 1 < characters.length) {
        printCharacterName(characters, idx + 1);
      }
    } else {
      console.log(error);
    }
  });
}
