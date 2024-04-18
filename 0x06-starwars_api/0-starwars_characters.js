#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const printCharacterNames = (characterUrls, index) => {
  if (index === characterUrls.length) return;
  
  request(characterUrls[index], function (err, res, body) {
    if (err) throw err;
    const characterData = JSON.parse(body);
    console.log(characterData.name);
    printCharacterNames(characterUrls, index + 1);
  });
};

request(`https://swapi-api.hbtn.io/api/films/${movieId}`, function (err, res, body) {
  if (err) throw err;
  
  const movieData = JSON.parse(body);
  const characterUrls = movieData.characters;
  printCharacterNames(characterUrls, 0);
});

