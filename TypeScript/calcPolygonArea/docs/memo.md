NL : 辺の個数, 1辺の長さ から外周円、内周円を計算
NCR: 辺の個数, 外接円の半径
NIR: 辺の個数, 内接円の半径


- posArray エッジ同士が交差するか判定
- 閉じた図形か判定
- posArray で firstPos, endPos の誤差を検出
  - 誤差の最大値:
    - Math.sqrt(polygonSize.width**2, polygonSize.height**2) * 0.0001
- 

Polygon
  type Coodinate: [number, number]
  coodinates: Coodinate[]
  polygonSize: Size
  type: "polygon"
  style: Style
  area        : number

RegularPolygon
  edgeLength  : number
  edgeNumber  : number
  perimeter   : number
  circumRadius: number
  inRadius    : number

  calc.area()
  calc.perimeter()
  calc.circumRadius()
  calc.inRadius()

Circle
  radius: number

RegularPolygon

Display
  constractor(selector)
  reset()
  update(inputName, value)

Style
  borderColor: string | null
  borderWidth: num | string
  backgroundColor: string | null


Canvas
  constractor(selector)
  reset()
  draw.circle(origin, r)
  draw.polygon(origin, points)


