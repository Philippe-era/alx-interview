#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request(url, async (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }

  if (res.statusCode !== 200) {
    console.error('Failed to fetch movie data:', res.statusCode);
    return;
  }

  try {
    const movieData = JSON.parse(body);
    const charactersArray = movieData.characters;

    for (const characterUrl of charactersArray) {
      await new Promise((resolve, reject) => {
        request(characterUrl, (err, res, body) => {
          if (err) {
            console.error(err);
            reject(err);
            return;
          }

          if (res.statusCode !== 200) {
            console.error(`Failed to fetch character data (${characterUrl}):`, res.statusCode);
            resolve();
            return;
          }

          const characterData = JSON.parse(body);
          console.log(characterData.name);
          resolve();
        });
      });
    }
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError);
  }
});
