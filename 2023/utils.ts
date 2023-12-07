const fs = require("fs");
export const parseFileToLinesArray = (filename: string): string[] => {
  return fs.readFileSync(filename, "utf8").split("\n");
};
