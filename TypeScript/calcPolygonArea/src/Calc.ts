import { XY, XYArray, Size } from "./Shape.js";

export class Calc {
  // 多角形が収まる矩形サイズを返す
  static polygonSize(xyArray: XYArray = []): Size {
    if (xyArray.length === 0) {
      return { width: 0, height: 0 };
    }
    if (xyArray.length === 0) {
      return { width: 0, height: 0 };
    }
    const xPoints = xyArray.map((point) => point.x);
    const yPoints = xyArray.map((point) => point.y);
    const size = {
      width : Math.max(...xPoints) - Math.min(...xPoints),
      height: Math.max(...yPoints) - Math.min(...yPoints),
    }
    return size;
  }

  // 座標法を用いて多角形の面積を返す
  static polygonArea(xyArray: XYArray = []): number {
    if (xyArray.length === 0) {
      return 0;
    }
    const n = xyArray.length;
    let area = 0;
    for (let i = 0; i < n; i++) {
      const point = xyArray[i];
      // 最後に呼ばれるnextPointは_coordinates[0]になる (剰余演算子を使用)
      const nextPoint = xyArray[(i + 1) % n];
      area += (point.x * nextPoint.y) - (nextPoint.x * point.y);
    }
    return area;
  }

  // 多角形の周長を返す
  static polygonPerimeter(xyArray: XYArray = []): number {
    if (xyArray.length === 0) {
      return 0;
    }
    const n = xyArray.length;
    let perimeter = 0;
    for (let i = 0; i < n; i++) {
      const point = xyArray[i];
      // 最後に呼ばれるnextPointは_coordinates[0]になる (剰余演算子を使用)
      const nextPoint = xyArray[(i + 1) % n];
      perimeter += Calc.distance(point, nextPoint);
    }
    return perimeter;
  }

  // 2点間の距離を返す
  static distance(p1: XY, p2: XY): number {
    return Math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2);
  }

  // 円の面積を返す
  static circleArea(radius: number = 0): number {
    if (radius) {
      return radius ** 2 * Math.PI;
    } else {
      return 0;
    }
  }

  // 円の周長を返す
  static circlePerimeter(radius: number = 0): number {
    if (radius) {
      return radius * 2 * Math.PI;
    } else {
      return 0;
    }
  }

}
