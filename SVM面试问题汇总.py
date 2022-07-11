1.什么是SVM?
答：考虑二分类问题，SVM就是要找到一个超平面可以把分类之间的margin扩展到最大。
2.支持向量机中的“支持向量”是什么?
答：某些最接近分类线或分类面的实例，此实例影响分类线或分类面的建立，甚至某种程度下影响
margin的大小。也就是说，我们移动非支持向量，分类线或分类面不变，当我们移动支持向量时，
分类线或分类面可能就改变了。
3.请描述软边界soft margin和硬边界hard margin之间的区别。
答：在分类问题中，硬边界就是此分类线或分类面会严格分类，比如一边是1类别，另一边是0类别，
没有0类别的点会出现在1类别那边。软边界需要考虑global balance，会考虑分类边界放置位置与
margin之间的trade off。即便某些点可能未分类正确，但整体情况应该是更好的。
4.请描述SVM中核函数是什么。
在构建超平面时，有时我们需要进行向量的点积，如果样本数量很多，这可能需要大量的运算空间，
核函数就是实现了与点积类似的功能却可以节省运算空间的一种方法。
5.请描述SVM里参数C的含义。
在软边界中，我们划分超平面要考虑margin和错误点之间的balance，有时，我们无法容忍错误点，
有时，我们可以牺牲一些错误点来增加margin。C就在某种程度上表示了我们对错误点的容忍度。
