#!/usr/bin/node
// Displays all the characters retrieved from the used Star Wars API

const request = require("request");
const args = process.argv;

if (args.length !== 3) {
  console.log("USAGE: ./<programName> <movieID>");
  process.exit(1);
}

const movieID = args[2];

function requestUrl(url) {
  return new Promise(function (resolve, reject) {
    request(url, function (err, res, body) {
      if (!err) {
        const jsonResp = JSON.parse(body);
        resolve(jsonResp);
      } else {
        reject(err);
      }
    });
  });
}

request(
  `https://swapi-api.alx-tools.com/api/films/${movieID}`,
  async function printCharacters(err, res, body) {
    if (err === null) {
      const jsonBody = JSON.parse(body);
      const character_urls = jsonBody["characters"];
      console.log(character_urls);

      let characters = [];
      for (const url of character_urls) {
        const person = await requestUrl(url);

        if (person) {
          console.log(person["name"]);
          //characters.push(person["name"]);
        }
      }

      //for (const name of characters) {
      //console.log(name);
      //}
    } else {
      console.error("error: ", err);
    }
  }
);
