#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const object = {};
request(url, function (err, resp, body) {
  if (resp.statusCode === 200) {
    for (const task of JSON.parse(body)) {
      if (task.completed) {
        if (object[task.userId]) {
          object[task.userId]++;
        } else {
          object[task.userId] = 1;
        }
      }
    }
  } else {
    console.log(err);
  }
  console.log(object);
});
