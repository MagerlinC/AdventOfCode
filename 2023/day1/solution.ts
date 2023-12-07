import { parseFileToLinesArray } from "../utils";

export const stringToFirstAndLastDigits = (input: string) => {
  const regex = new RegExp(/\d+/g);
  const matches: string[] = input.match(regex) || [];
  if (matches.length === 0) return [];
  const firstNumber = matches[0];
  const lastNumber = matches[matches.length - 1];
  return [firstNumber[0], lastNumber[lastNumber.length - 1]];
};

export const solution = (lines: string[]) => {
  let sum = 0;
  lines.forEach((line) => {
    const digits = stringToFirstAndLastDigits(line);
    const firstDigit = digits[0];
    const lastDigit = digits[1];
    sum += parseInt(`${firstDigit}${lastDigit}`);
  });
  return sum;
};

const input = parseFileToLinesArray("day1/input.txt");
console.log(solution(input));
