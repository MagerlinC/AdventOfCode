import { solution, stringToFirstAndLastDigits } from "./solution";

test("String to digits returns correct digits for 1abc2", () => {
  expect(stringToFirstAndLastDigits("1abc2")).toStrictEqual(["1", "2"]);
});

test("String to digits returns correct digits for pqr3stu8vwx", () => {
  expect(stringToFirstAndLastDigits("pqr3stu8vwx")).toStrictEqual(["3", "8"]);
});

test("String to digits returns correct digits for treb7uchet", () => {
  expect(stringToFirstAndLastDigits("treb7uchet")).toStrictEqual(["7", "7"]);
});

test("String to digits returns correct digits for tfn5kx6twojmzgbdznc2", () => {
  expect(stringToFirstAndLastDigits("tfn5kx6twojmzgbdznc2")).toStrictEqual([
    "5",
    "2",
  ]);
});

test("String to digits returns correct digits for nx9ninekvzzdlncblkdqbgspdfkcx", () => {
  expect(
    stringToFirstAndLastDigits("nx9ninekvzzdlncblkdqbgspdfkcx")
  ).toStrictEqual(["9", "9"]);
});

test("String to digits returns correct digits for zmkrnqfgpvlfknseven555oneightrgp", () => {
  expect(
    stringToFirstAndLastDigits("zmkrnqfgpvlfknseven555oneightrgp")
  ).toStrictEqual(["5", "5"]);
});

test("Solution returns 142 for example", () => {
  const input = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"];
  expect(solution(input)).toBe(142);
});
