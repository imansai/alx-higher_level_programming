#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = 'https://swapi.dev/api/films/';
request.get(apiUrl + movieId, function (filmError, filmResponse, filmBody) {
  if (filmError) {
    console.log('Error fetching film details:', filmError);
  } else {
    const filmData = JSON.parse(filmBody);
    const characterUrls = filmData.characters;
    characterUrls.forEach(function (characterUrl) {
      request.get(characterUrl, function (charError, charResponse, charBody) {
        if (charError) {
          console.log('Error fetching character details:', charError);
        } else {
          const characterData = JSON.parse(charBody);
          console.log('Character Name:', characterData.name);
        }
      });
    });
  }
});

