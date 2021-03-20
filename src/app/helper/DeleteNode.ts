import { Node } from './Node';

export const deleteNodeInTree = (cur: Node, parent: Node) => {
  if (cur === null || parent === null) return null;

  if (parent.left === cur) {
    parent.left = null;
  } else {
    parent.right = null;
  }

  return null;
};
