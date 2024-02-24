import { XY } from "./Shape.js";
import { Calc } from "./Calc.js"
import { Style } from "./Style.js";

export class Circle {
  private _style    : Style;   // 描画設定 get
  private _origin   : XY;      // 原点     get set
  private _radius   : number;  // 半径     get set
  private _area     : number;  // 面積     get
  private _perimeter: number;  // 周長     get

  constructor(radius: number) {
    this._style     = new Style();
    this._origin    = { x: 0, y: 0 };
    this._radius    = radius;
    this._area      = this.calc.area();
    this._perimeter = this.calc.perimeter();
  }

  readonly calc = {
    area     : Calc.circleArea,
    perimeter: Calc.circlePerimeter,
  }

  // setter
  set origin(xy: XY)    { this._origin = xy; }
  set radius(r: number) { this._radius = r;  }

  // getter
  get style       (): Style   { return this._style;     }
  get origin      (): XY      { return this._origin;    }
  get radius      (): number  { return this._radius;    }
  get area        (): number  { return this._area;      }
  get perimeter   (): number  { return this._perimeter; }
  
}