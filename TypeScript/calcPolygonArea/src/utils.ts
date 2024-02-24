export type Params = {
  [K: string]: any;
};

export function consoleLogInfo(params: Params) {
  console.clear();
  for (const key in params) {
    console.log(key, params[key]);
  }
}
