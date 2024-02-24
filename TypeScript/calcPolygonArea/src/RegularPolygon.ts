import { Polygon, XY, XYArray, Size } from "./Shape.js";
import { Calc } from "./Calc.js"
import { Style } from "./Style.js";

// export type RegularPolygonItems = keyof RegularPolygon;
// ↑setterのプロパティ名だけを抽出してユニオン型にしたい
export type RegularPolygonItems = "lineLength" | "lineNumber";

export class RegularPolygon implements Polygon {
  private _style        : Style;    // 描画設定      get
  private _origin       : XY;       // 辺の個数      get set
  private _xyArray      : XYArray;  // 格点座標      get set
  private _size         : Size;     // 矩形サイズ    get
  private _area         : number;   // 面積          get
  private _perimeter    : number;   // 周長          get
  private _lineNumber   : number;   // 辺の個数      get set
  private _lineLength   : number;   // 1辺の長さ     get set
  private _circumRadius : number;   // 外接円の半径  get
  private _inRadius     : number;   // 内接円の半径  get

  constructor(lineNumber: number, lineLength: number) {
    this._style        = new Style();
    this._origin       = { x: 0, y: 0 };
    this._xyArray      = [];
    this._size         = this.calc.size();
    this._area         = this.calc.area();
    this._perimeter    = this.calc.perimeter();
    this._lineNumber   = lineNumber;
    this._lineLength   = lineLength;
    this._circumRadius = 0;
    this._inRadius     = 0;
    this.calcAll();
  }

  readonly calc = {
    size     : Calc.polygonSize,
    area     : Calc.polygonArea,
    perimeter: Calc.polygonPerimeter,
    distance : Calc.distance,

    // lineNumber, lineLength から外周円を計算
    circumRadius: (lineNumber: number, lineLength: number) => {
      const devidedAngleRad = (Math.PI * 2) / lineNumber;
      return lineLength / 2 / Math.sin(devidedAngleRad / 2);
    },

    // lineNumber, lineLength から内周円を計算
    inRadius: (lineNumber: number, lineLength: number) => {
      return lineLength / 2 / Math.tan(Math.PI / lineNumber);
    },

    // lineNumber, circumRadius から多角形の座標を計算
    xyArray: (lineNumber: number, circumRadius: number) => {
      const radians = Array.from(
        { length: lineNumber }, (_, i) => (i / lineNumber) * Math.PI * 2
      );
      const xyArray = radians.map((rad) => (
        {
          x: circumRadius * Math.cos(rad - Math.PI / 2),
          y: circumRadius * Math.sin(rad - Math.PI / 2),
        }
      ));
      return xyArray;
    },
  }

  calcAll() {
    this._circumRadius = this.calc.circumRadius(this.lineNumber, this.lineLength);
    this._inRadius     = this.calc.inRadius    (this.lineNumber, this.lineLength);
    this._xyArray      = this.calc.xyArray     (this.lineNumber, this.circumRadius);
    this._size         = this.calc.size        (this.xyArray);
    this._area         = this.calc.area        (this.xyArray);
    this._perimeter    = this.calc.perimeter   (this.xyArray);
  }
  
  // setter
  set origin(xy: XY) {
    this._origin = xy;
  }
  set xyArray(array: XYArray) {
    if (array.length) {
      this._xyArray = array;
      this.calcAll();
    }
  }
  set lineNumber(num: number) {
    if (num >= 3) {
      this._lineNumber = num;
      this.calcAll();
    }
  }
  set lineLength(len: number) {
    if (len > 0) {
      this._lineLength = len;
      this.calcAll();
    }
  }

  // getter
  get style       (): Style   { return this._style;        }
  get origin      (): XY      { return this._origin;       }
  get xyArray     (): XYArray { return this._xyArray;      } 
  get size        (): Size    { return this._size;         }
  get area        (): number  { return this._area;         }
  get perimeter   (): number  { return this._perimeter;    }   
  get lineNumber  (): number  { return this._lineNumber;   }  
  get lineLength  (): number  { return this._lineLength;   }  
  get circumRadius(): number  { return this._circumRadius; }
  get inRadius    (): number  { return this._inRadius;     }    
}
