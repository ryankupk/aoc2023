let sessionId =
  "";
let url = "https://adventofcode.com/2022/day/1/input";

function SolvePartOne(data) {
  let calories = data.split("\n");
  let elves = {};
  let cur_elf = 0;
  let max_elf = -1;
  let max_calories = -1;
  for (let calorie of calories) {
    if (calorie != "") {
      if (elves[cur_elf] == undefined) {
        elves[cur_elf] = Number(calorie);
      } else {
        elves[cur_elf] += Number(calorie);
      }
    } else {
      if (elves[cur_elf] > max_calories) {
        max_elf = cur_elf;
        max_calories = elves[cur_elf];
      }
      cur_elf++;
    }
  }
  return max_calories;
}
function SolvePartOneUtility(data) {
  let calories = data.split("\n");
  let elves = {};
  let cur_elf = 0;
  let max_elf = -1;
  let max_calories = -1;
  for (let calorie of calories) {
    if (calorie != "") {
      if (elves[cur_elf] == undefined) {
        elves[cur_elf] = Number(calorie);
      } else {
        elves[cur_elf] += Number(calorie);
      }
    } else {
      if (elves[cur_elf] > max_calories) {
        max_elf = cur_elf;
        max_calories = elves[cur_elf];
      }
      cur_elf++;
    }
  }
  return elves;
}

function SolvePartTwo(data) {
  let elves = SolvePartOneUtility(data);
  let sortedElves = Object.values(elves).sort();
  console.log(sortedElves.slice(-20));
  return sortedElves.slice(-5, -2).reduce((partialSum, a) => partialSum + a, 0);
}

fetch(url, {
  headers: {
    "Cookie": "session=" + sessionId,
  },
})
  .then((response) => {
    return response.text();
  })
  .then((data) => {
    console.log(SolvePartOne(data));
    console.log(SolvePartTwo(data));
  });
