import { Style } from "./Style.js";

export type XY  = { x: number; y: number };
export type XYArray = XY[];
export type Size = { width: number; height: number };

export interface Polygon {
  readonly style: Style,
  origin   : XY,
  xyArray  : XYArray,
  size     : Size,
  area     : number,
  perimeter: number,
  readonly calc: FunctionObject
}

interface FunctionObject {
  [key: string]: Function;
}

export interface Circle {
  readonly style: Style,
  origin   : XY,
  size     : Size,
  area     : number,
  perimeter: number,
  readonly calc: FunctionObject
}
