// pages/search2/search2.js
const app = getApp()
var id = 0;
Page({

  /**
   * 页面的初始数据
   */
  data: {
    searchShow: [],
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onLoad: function (options) {
    id = options.classifyId;
    this.getItem()
    console.log(id)
  },
  getItem:function (options)
  {
    var that = this;
    wx.request({
    method: 'GET',
      url: 'http://www.mallproject.cn:8000/api/item/?item_sub_category=' + id,
      success: function (res) {
        that.setData({
          searchShow: res.data,
        })
        if (res.data.length == 0) {
          wx.showToast({
            title: '无相关商品',
            icon: 'none',
            duration: 1500
          })
          wx.redirectTo({
            url: '../classify/classify',
          })
        }
        
      }
    })
  },
  catchTapCategory: function (e) {
    //用来处理商品本身的tap id
    var that = this;
    var goodsId = e.currentTarget.dataset.goodsid;
    console.log('goodsId:' + goodsId);
    //新增商品用户点击数量
    //that.goodsClickShow(goodsId);
    //跳转商品详情
    wx.navigateTo({ url: '../detail/detail?goodsId=' + goodsId })
  },
  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})