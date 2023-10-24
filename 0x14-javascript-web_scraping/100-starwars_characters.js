#!/usr/bin/node

const request = require('request');
const filmId = process.argv[2];
const filmsApiUrl = 'https://swapi-api.hbtn.io/api/films/';

request.get(filmsApiUrl + filmId, function (errorFilm, responseFilm, bodyFilm) {
  if (errorFilm) {
    console.log('Error fetching film details:', errorFilm);
  } else {
    const filmDetails = JSON.parse(bodyFilm);
    const charactersUrls = filmDetails.characters;

    charactersUrls.forEach(function (characterUrl) {
      request.get(characterUrl, function (errorCharacter, responseCharacter, bodyCharacter) {
        if (errorCharacter) {
          console.log('Error fetching character details:', errorCharacter);
        } else {
          const characterDetails = JSON.parse(bodyCharacter);
          console.log('Character Name:', characterDetails.name);
        }
      });
    });
  }
});
