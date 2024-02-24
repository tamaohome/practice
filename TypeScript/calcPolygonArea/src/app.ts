import { RegularPolygon } from "./RegularPolygon";
import { Circle } from "./Circle";
import { DisplayItem } from "./Display";
import { Canvas } from "./Canvas";
import { consoleLogInfo } from "./utils";

class App {
  lineNumber: number;
  lineLength: number;
  polygon: RegularPolygon;
  circumCircle: Circle;
  inCircle: Circle;
  displayItem: DisplayItem;
  canvas: Canvas;

  constructor() {
    this.lineNumber = 5; // default
    this.lineLength = 100; // default
    this.polygon = new RegularPolygon(this.lineNumber, this.lineLength);
    this.circumCircle = new Circle(this.polygon.circumRadius);
    this.inCircle = new Circle(this.polygon.inRadius);
    this.displayItem = new DisplayItem("#inputForm");
    this.canvas = new Canvas("#canvas", [this.polygon], 320, 320);
    consoleLogInfo(this);
    //                       id               value                       digit detail          symbol  readonly
    this.displayItem.addItem("lineNumber",    this.lineNumber,            0,    "辺の個数",     "n");
    this.displayItem.addItem("lineLength",    this.lineLength,            3,    "1辺の長さ",    "L");
    this.displayItem.addItem("area",          this.polygon.area,          3,    "面積",         "S",    true);
    this.displayItem.addItem("perimeter",     this.polygon.perimeter,     3,    "周長",         "n*L",  true);
    this.displayItem.addItem("circumRadius",  this.polygon.circumRadius,  3,    "外周円の半径", "r1",   true);
    this.displayItem.addItem("inRadius",      this.polygon.inRadius,      3,    "内周円の半径", "r2",   true);
    this.displayItem.createInputForms();
    this.displayItem.update(this.polygon);

    // 入力イベント
    this.displayItem.handleInputChange(this.polygon, this.canvas, "lineNumber");
    this.displayItem.handleInputChange(this.polygon, this.canvas, "lineLength");
  }
}

new App();
