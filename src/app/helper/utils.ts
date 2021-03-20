export const trim = (list: any[], X: string) => {
  const N = list.length;
  for (let index = N - 1; index >= 0; index--) {
    if (list[index] === X) {
      list.pop();
    } else {
      return;
    }
  }
};

export const arrayToString = (lst: any[], Seperator: string) => {
  const N = lst.length;
  let string = '';
  lst.forEach((item, index) => {
    if (index < N - 1) {
      string += item + Seperator;
    } else {
      string += item;
    }
  });
  return string;
};
