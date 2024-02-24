// type Item = {
//   id: string,
//   value: string | number,
//   element?: HTMLElement
// }

// import { Polygon } from "./Shape.js";
import { RegularPolygon, RegularPolygonItems } from "./RegularPolygon.js";
import { Canvas } from "./Canvas.js";

interface InputObject {
  // ID (ex. circumRadius)
  [id: string]: InputItem;
}
interface InputItem {
  value   : number,  // 値
  digit   : number,  // 表示桁数(小数第n位)
  label   : string,  // 表示名 (ex. 外接円の半径)
  symbol  : string,  // 記号   (ex. r1)
  readonly: boolean, // 入力不可/入力可
  element?: HTMLInputElement
}

// interface MessageObject {
//   [key: string]: {
//     key: string,
//     message: string,
//     element: HTMLElement
//   };
// }

export class DisplayItem {
  readonly rootElement: HTMLElement;
  readonly itemObj: InputObject;
  
  constructor(selector: string) {
    this.rootElement = document.querySelector(selector) as HTMLElement;
    this.itemObj = {};
  }

  // itemObj[id]を基にインプットフォームを作成
  createInputForms() {
    for (const id in this.itemObj) {
      const symbolTag = this.itemObj[id].symbol ? `<span class="symbol">${this.itemObj[id].symbol}</span>` : "";
      this.rootElement.insertAdjacentHTML("beforeend", `
      <div class="input-item">
        <label for="${id}">${this.itemObj[id].label}${symbolTag}</label>
        <input type="text" name="${id}" id="${id}"${this.itemObj[id].readonly ? " readonly" : ""}>
      </div>
      `);
      const element = document.querySelector("#" + id);
      if (element instanceof HTMLInputElement) {
        this.itemObj[id].element = element;
      }
    }
  }

  // rootElementを初期化
  clearHTML(): void {
    if (this.rootElement) {
      while (this.rootElement.firstChild) {
        this.rootElement.removeChild(this.rootElement.firstChild);
      }
    }
  }

  addItem(id      : string,
          value   : number,
          digit   : number  = 0,
          label   : string  = "",
          symbol  : string  = "",
          readonly: boolean = false): void {
    const item: InputItem = {
      value   : value,
      digit   : digit,
      element : this.rootElement.querySelector("#" + id) as HTMLInputElement,
      label   : label || id,
      symbol  : symbol,
      readonly: readonly,
    }
    this.itemObj[id] = item;
  }

  // HTMLInputElementの内容を更新
  update(polygon: RegularPolygon): void {
    for (const id in this.itemObj) {
      // polygonインスタンスの最新値をitemObjインスタンスに反映
      const newValue = polygon[id as keyof RegularPolygon];
      if (typeof newValue === "number") {
        this.itemObj[id].value = newValue;
      }
      // 値を<input>に反映
      const element = this.itemObj[id].element;
      if (element instanceof HTMLInputElement) {
        element.value = this.roundDecimal(this.itemObj[id].value, this.itemObj[id].digit);
      }
    }
  }

  // 桁丸め
  roundDecimal(value: number, digit: number): string {
    if (digit === 0) {
      return Math.round(value).toString();
    }
    return (Math.round(value * Math.pow(10, digit)) / Math.pow(10, digit)).toFixed(digit);
  }

  // 入力イベント
  handleInputChange(polygon: RegularPolygon, canvas: Canvas, id: RegularPolygonItems) {
    //                                       ↓"input"だと1文字入力毎に発火してしまう
    this.itemObj[id].element!.addEventListener("change", (event: Event) => {
      const target = event.target as HTMLInputElement;
      this.itemObj[id].value = Number(target.value);
      polygon[id] = Number(target.value);
      polygon.calcAll();
      this.update(polygon);
      canvas.update([polygon]);
    });

  }
}

// export class DisplayMessage {
//   private _rootElement: HTMLElement;
//   private _messageObj: object;

//   constructor(element: HTMLElement) {
//     this._rootElement = element;
//   }

//   // getter
//   get messages(): object { return this._messageObj; }
// }
