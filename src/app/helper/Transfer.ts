import { Node } from './Node';
import { arrayToString, trim } from './utils';

export class Transfer {
  private X = 'NA';
  private Seperator = '|';
  private serializeHelper(root: Node, lst: string[]) {
    if (!root) {
      lst.push(this.X);
      return;
    }
    // Pre-Order traversal
    lst.push(root.val);
    this.serializeHelper(root.left, lst);
    this.serializeHelper(root.right, lst);
  }

  serialize(root: Node) {
    var lst = [];
    this.serializeHelper(root, lst);
    trim(lst, this.X);
    const string = arrayToString(lst, this.Seperator);
    return string;
  }

  private deserializeHelper(lst: string[]) {
    if (lst.length < 1) {
      return null;
    }

    let val = lst.shift();

    if (val === this.X) {
      return null;
    }

    var root = new Node(val);
    root.left = this.deserializeHelper(lst);
    root.right = this.deserializeHelper(lst);
    return root;
  }

  deserialize(data: string) {
    if (!data || data.length === 0) {
      return null;
    }

    return this.deserializeHelper(data.split(this.Seperator));
  }
}
