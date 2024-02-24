export class Style {
  static DEFAULT_BACKGROUND_COLOR = "#fff";
  static DEFAULT_BORDER_COLOR = "#000";

  private _borderColor    : string | null;
  private _borderWidth    : number;
  private _backgroundColor: string | null;

  constructor() {
    this._borderColor     = Style.DEFAULT_BORDER_COLOR;
    this._borderWidth     = 1;
    this._backgroundColor = Style.DEFAULT_BACKGROUND_COLOR;
  }
  
  // setter
  set borderColor(color: string | null) {
    this._borderColor = this.isColor(color) ? color : null;
  }
  set borderWidth(width: number) {
    this._borderWidth = width >= 0 ? width : 0;
  }
  set backgroundColor(color: string | null) {
    this._backgroundColor = this.isColor(color) ? color : null;
  }

  // getter
  get borderColor(): string {
    return this._borderColor || Style.DEFAULT_BORDER_COLOR;
  }
  get borderWidth(): number {
    return this._borderWidth;
  }
  get backgroundColor(): string {
    return this._backgroundColor || Style.DEFAULT_BORDER_COLOR;
  }

  isColor(color: string | null): boolean {
    if (color) {
      return color.match(/^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$/) !== null;
    } else {
      return false;
    }
  }
}
