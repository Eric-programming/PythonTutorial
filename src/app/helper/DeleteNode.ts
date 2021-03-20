import { Node } from './Node';

export const deleteNodeInTree = (
  cur: Node,
  parent: Node,
  isOnLeft: boolean
) => {
  //cur is leaf node
  if (cur === null || (cur.left === null && cur.right === null)) return null;

  //find replacement
  let replace = null;
  if (cur.right !== null) {
    replace = cur.right;
  } else if (cur.left !== null) {
    replace = cur.left;
  }

  //parent is null
  if (parent === null) return replace;

  if (isOnLeft) {
    parent.left = replace;
  } else {
    parent.right = replace;
  }

  return replace;
};
