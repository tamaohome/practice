import { XY, XYArray, Size } from "./Shape.js";
import { RegularPolygon } from "./RegularPolygon.js";

export class Canvas {
  readonly DEFAULT_SIZE = 150;

  private _rootElement: HTMLCanvasElement;
  private _size       : Size;
  private _origin     : XY;

  constructor(selector: string, polygonArray: RegularPolygon[], width: number, height: number) {
    this._size = { width, height };
    this._origin = {
      x: Math.round(this._size.width / 2),
      y: Math.round(this._size.height / 2),
    };

    this._rootElement = document.querySelector(selector) as HTMLCanvasElement;
    this._rootElement.setAttribute("style", "background-color: whitesmoke;");
    this._rootElement.setAttribute("width", this._size.width.toString());
    this._rootElement.setAttribute("height", this._size.height.toString());

    this.update(polygonArray);
  }

  clear(): void {
    while (this._rootElement.firstChild) {
      this._rootElement.removeChild(this._rootElement.firstChild);
    }
  }
  
  update(polygonArray: RegularPolygon[]): void {
    this.clear();
    for (const polygon of polygonArray) {
      this.drawPolygon(polygon.xyArray);
      this.drawCircle("circumCircle", polygon.circumRadius);
      this.drawCircle("inCircle", polygon.inRadius);
    }
  }

  // 多角形を描画
  drawPolygon(xyArray: XYArray): void {
    const element = document.createElementNS("http://www.w3.org/2000/svg", "polygon");
    element.setAttribute("id", "poly");
    const points = xyArray
      .map((point) => `${this._origin.x + point.x} ${this._origin.y + point.y}`)
      .join(", ");
    element.setAttribute("points", points);
    element.setAttribute("stroke", "#353c4e");
    element.setAttribute("fill", "white");
    this._rootElement.appendChild(element);
  }

  // 円を描画
  drawCircle(id: string, radius: number) {
    const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    circle.setAttribute("id", id);
    circle.setAttribute("cx", `${this._origin.x}`);
    circle.setAttribute("cy", `${this._origin.y}`);
    circle.setAttribute("r", radius.toString());
    circle.setAttribute("stroke", "#353c4e");
    circle.setAttribute("fill", "none");
    this._rootElement.appendChild(circle);
  }
}