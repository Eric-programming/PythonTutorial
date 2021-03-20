export class Node {
  val: string;
  left: Node;
  right: Node;
  key: string;
  constructor(val: string, key: string) {
    this.val = val;
    this.key = key;
  }
}
