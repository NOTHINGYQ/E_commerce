# Generated by Django 2.2 on 2019-09-05 14:11

from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('brand_id', models.AutoField(primary_key=True, serialize=False, verbose_name='商品品牌')),
                ('brand_name', models.CharField(blank=True, max_length=10, null=True, verbose_name='品牌')),
            ],
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('coupon_id', models.AutoField(primary_key=True, serialize=False, verbose_name='优惠券')),
                ('coupon_off', models.IntegerField(default=0, verbose_name='减多少元')),
                ('coupon_require', models.IntegerField(default=100, verbose_name='满多少元')),
                ('coupon_last', models.DurationField(verbose_name='有效期')),
            ],
        ),
        migrations.CreateModel(
            name='Evaluate',
            fields=[
                ('evaluate_id', models.AutoField(primary_key=True, serialize=False, verbose_name='评价')),
                ('evaluate_TJUCarat', models.IntegerField(default=10, verbose_name='评价完成所获得洋克拉')),
                ('evaluate_isAnonymous', models.BooleanField(default=False, verbose_name='评价是否匿名')),
                ('evaluate_content', models.CharField(blank=True, max_length=100, null=True, verbose_name='评价内容')),
                ('evaluate_item_score', models.IntegerField(default=5, verbose_name='商品评价')),
                ('evaluate_express_package', models.IntegerField(default=5, verbose_name='物流包装评价')),
                ('evaluate_express_speed', models.IntegerField(default=5, verbose_name='物流速度评价')),
                ('evaluate_express_service', models.IntegerField(default=5, verbose_name='物流服务评价')),
                ('evaluate_create_time', models.DateField(auto_now_add=True, verbose_name='评价时间')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('group_id', models.AutoField(primary_key=True, serialize=False, verbose_name='组')),
                ('group_name', models.CharField(default='none', max_length=30, verbose_name='组名')),
                ('group_info', models.CharField(default='这个群主有点懒~', max_length=30, verbose_name='组简介')),
                ('group_create_time', models.DateField(auto_now_add=True, verbose_name='组创建时间')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False, verbose_name='商品编号')),
                ('item_name', models.CharField(default='none', max_length=100, verbose_name='品名')),
                ('item_price', models.DecimalField(decimal_places=3, default='none', max_digits=100, verbose_name='价格')),
                ('item_stoke', models.IntegerField(default=9999, verbose_name='库存')),
                ('item_preview_image', stdimage.models.StdImageField(default='item/previewImage/itemDefault.jpg', upload_to='item/previewImage', verbose_name='商品预览图')),
                ('item_browse', models.IntegerField(default=0, verbose_name='浏览量')),
                ('item_off', models.CharField(default=' ', max_length=10, verbose_name='优惠信息')),
                ('item_prePrice', models.DecimalField(decimal_places=3, default=0, max_digits=100, verbose_name='商品原价')),
                ('item_sale', models.IntegerField(default=0, verbose_name='销量')),
                ('item_create_time', models.DateField(auto_now_add=True, verbose_name='商品上架时间')),
                ('item_VIPOff', models.IntegerField(default=10, verbose_name='会员减价')),
                ('item_trade_amount', models.IntegerField(blank=True, default=0, null=True, verbose_name='交易数量')),
                ('item_brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='backends.Brand', verbose_name='品牌')),
            ],
        ),
        migrations.CreateModel(
            name='ItemCategory',
            fields=[
                ('item_category_id', models.AutoField(primary_key=True, serialize=False, verbose_name='商品大类')),
                ('item_category', models.CharField(default='none', max_length=100, unique=True, verbose_name='类别')),
                ('item_category_isHaveSub', models.BooleanField(default=False, verbose_name='是否有子类')),
                ('item_category_image', models.ImageField(default='category/category_image/itemDefault.jpg', upload_to='category/category_image', verbose_name='轮播图')),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_name', models.CharField(default='none', max_length=30, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('store_id', models.AutoField(primary_key=True, serialize=False, verbose_name='商店')),
                ('store_name', models.CharField(default='none', max_length=100, verbose_name='店名')),
                ('store_contact_info', models.CharField(default='none', max_length=30, verbose_name='联系方式')),
                ('store_info', models.CharField(default='这个店主有点懒~', max_length=100, verbose_name='店铺简介')),
                ('store_evaluate', models.DecimalField(decimal_places=1, default=10.0, max_digits=10, verbose_name='店铺评价')),
                ('store_create_time', models.DateField(auto_now_add=True, verbose_name='店铺创建时间')),
            ],
        ),
        migrations.CreateModel(
            name='SystemMessage',
            fields=[
                ('message_id', models.AutoField(primary_key=True, serialize=False, verbose_name='系统消息')),
                ('message_content', models.CharField(default='none', max_length=100, verbose_name='消息内容')),
                ('message_type', models.IntegerField(default=0, verbose_name='消息类型')),
                ('message_create_time', models.DateField(auto_now_add=True, verbose_name='系统消息创建时间')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False, verbose_name='用户')),
                ('user_nickname', models.CharField(default='none', max_length=30, unique=True, verbose_name='昵称')),
                ('user_password', models.CharField(default='123456', max_length=18, verbose_name='密码')),
                ('user_sex', models.CharField(default='男', max_length=1, verbose_name='性别')),
                ('user_tel', models.CharField(default='0', max_length=10, verbose_name='手机号')),
                ('user_headImage', stdimage.models.StdImageField(default='user/headImage/headDefault.jpg', upload_to='user/headImage', verbose_name='头像')),
                ('user_isAdmin', models.BooleanField(default=False, verbose_name='用户是否为管理员')),
                ('user_isBindQQ', models.BooleanField(default=False, verbose_name='用户是否绑定QQ')),
                ('user_location', models.CharField(default='中国', max_length=30, verbose_name='位置')),
                ('user_location_x', models.DecimalField(decimal_places=5, default=0, max_digits=100, verbose_name='用户经度')),
                ('user_location_y', models.DecimalField(decimal_places=5, default=0, max_digits=100, verbose_name='用户纬度')),
                ('user_TJUCarat', models.IntegerField(default=0, verbose_name='洋克拉')),
                ('user_isVIP', models.BooleanField(default=False, verbose_name='用户是否为VIP')),
                ('user_email', models.CharField(default='none', max_length=30, verbose_name='邮箱')),
                ('user_coupon', models.ManyToManyField(blank=True, null=True, to='backends.Coupon', verbose_name='用户持有的优惠券')),
            ],
        ),
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('trade_id', models.AutoField(primary_key=True, serialize=False, verbose_name='交易记录')),
                ('trade_amount', models.IntegerField(default=1, verbose_name='数量')),
                ('trade_isEvaluate', models.BooleanField(default=False, verbose_name='该交易是否已评价')),
                ('trade_create_time', models.DateField(auto_now_add=True, verbose_name='交易创建时间')),
                ('trade_finish_time', models.DateField(auto_now=True, verbose_name='交易完成时间')),
                ('trade_info', models.IntegerField(default=0, verbose_name='发货信息')),
                ('trade_TJUCarat', models.IntegerField(default=10, verbose_name='洋克拉')),
                ('trade_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backends.Item', verbose_name='交易商品')),
                ('trade_store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backends.Store', verbose_name='交易商店')),
                ('trade_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backends.User', verbose_name='用户')),
            ],
        ),
        migrations.CreateModel(
            name='StoreFollow',
            fields=[
                ('follow_id', models.AutoField(primary_key=True, serialize=False, verbose_name='店铺关注信息')),
                ('follow_store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backends.Store', verbose_name='关注店铺')),
                ('follow_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backends.User', verbose_name='关注者')),
            ],
        ),
        migrations.AddField(
            model_name='store',
            name='store_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backends.User', verbose_name='店主'),
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('cart_id', models.AutoField(primary_key=True, serialize=False, verbose_name='购物车')),
                ('cart_item_amount', models.IntegerField(default=1, verbose_name='商品数')),
                ('cart_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backends.Item', verbose_name='购物车商品')),
                ('cart_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backends.User', verbose_name='用户')),
            ],
        ),
        migrations.CreateModel(
            name='SearchRecord',
            fields=[
                ('record_id', models.AutoField(primary_key=True, serialize=False, verbose_name='搜索历史记录')),
                ('record_content', models.CharField(max_length=100, verbose_name='搜索内容')),
                ('record_flag', models.IntegerField(default=0, verbose_name='修改标志位')),
                ('record_create_time', models.DateTimeField(auto_now=True, verbose_name='搜索记录创建时间')),
                ('record_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backends.User', verbose_name='隶属哪个用户')),
            ],
        ),
        migrations.CreateModel(
            name='ItemSubCategory',
            fields=[
                ('item_subCategory_id', models.AutoField(primary_key=True, serialize=False, verbose_name='商品子类')),
                ('item_subCategory', models.CharField(default='none', max_length=100, unique=True, verbose_name='子类')),
                ('item_subCategory_image', stdimage.models.StdImageField(default='category/image/itemDefault.jpg', upload_to='category/image', verbose_name='子类图')),
                ('item_subCategory_belong', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='backends.ItemCategory', verbose_name='该子类隶属哪个大类')),
            ],
        ),
        migrations.CreateModel(
            name='ItemFollow',
            fields=[
                ('follow_id', models.AutoField(primary_key=True, serialize=False, verbose_name='商品关注信息')),
                ('follow_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backends.Item', verbose_name='关注商品')),
                ('follow_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backends.User', verbose_name='关注者')),
            ],
        ),
        migrations.CreateModel(
            name='ItemDetailImage',
            fields=[
                ('image_id', models.AutoField(primary_key=True, serialize=False, verbose_name='商品详情图')),
                ('image_url', models.ImageField(upload_to='item/detailImage', verbose_name='详情图')),
                ('image_belong', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backends.Item', verbose_name='隶属哪个商品')),
            ],
        ),
        migrations.CreateModel(
            name='ItemBannerImage',
            fields=[
                ('image_id', models.AutoField(primary_key=True, serialize=False, verbose_name='商品轮播图')),
                ('image_url', models.ImageField(upload_to='item/bannerImage', verbose_name='轮播图')),
                ('image_belong', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backends.Item', verbose_name='隶属哪个商品')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='item_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='backends.ItemCategory', verbose_name='类别'),
        ),
        migrations.AddField(
            model_name='item',
            name='item_store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backends.Store', verbose_name='所属商店'),
        ),
        migrations.AddField(
            model_name='item',
            name='item_sub_category',
            field=models.ForeignKey(on_delete=models.SET(1), to='backends.ItemSubCategory', verbose_name='子类'),
        ),
        migrations.CreateModel(
            name='GroupFollow',
            fields=[
                ('follow_id', models.AutoField(primary_key=True, serialize=False, verbose_name='组关注信息')),
                ('follow_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backends.Group', verbose_name='组')),
                ('follow_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backends.User', verbose_name='组员')),
            ],
        ),
        migrations.CreateModel(
            name='EvaluateImage',
            fields=[
                ('image_id', models.AutoField(primary_key=True, serialize=False, verbose_name='评价图片')),
                ('image_url', models.ImageField(upload_to='evaluate/image', verbose_name='评价图')),
                ('image_belong', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backends.Evaluate', verbose_name='隶属哪个评价')),
            ],
        ),
        migrations.AddField(
            model_name='evaluate',
            name='evaluate_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backends.Item', verbose_name='评价的商品'),
        ),
        migrations.AddField(
            model_name='evaluate',
            name='evaluate_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backends.User', verbose_name='评价的用户'),
        ),
        migrations.CreateModel(
            name='DailyOffItem',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False, verbose_name='每日特价商品')),
                ('item_off_create_time', models.DateField(auto_now_add=True, verbose_name='特价商品创建时间')),
                ('item_off_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backends.Item', verbose_name='特价商品id')),
            ],
        ),
        migrations.AddField(
            model_name='coupon',
            name='coupon_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backends.ItemCategory', verbose_name='适用大类'),
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('collection_id', models.AutoField(primary_key=True, serialize=False, verbose_name='收藏夹')),
                ('collection_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backends.Item', verbose_name='收藏的商品')),
                ('collection_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backends.User', verbose_name='隶属哪个用户')),
            ],
        ),
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('message_id', models.AutoField(primary_key=True, serialize=False, verbose_name='聊天信息')),
                ('message_type', models.IntegerField(default=0, verbose_name='信息类型')),
                ('message_create_time', models.DateField(auto_now_add=True, verbose_name='消息创建时间')),
                ('message_content', models.CharField(default='none', max_length=100, verbose_name='消息内容')),
                ('message_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='backends.Group', verbose_name='群组')),
                ('message_ori', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='message_ori', to='backends.User', verbose_name='发起者')),
                ('message_rec', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='message_rec', to='backends.User', verbose_name='接收者')),
            ],
        ),
        migrations.CreateModel(
            name='BrowseRecord',
            fields=[
                ('record_id', models.AutoField(primary_key=True, serialize=False, verbose_name='浏览历史记录')),
                ('record_flag', models.IntegerField(default=0, verbose_name='修改标志位')),
                ('record_create_time', models.DateTimeField(auto_now=True, verbose_name='浏览记录创建时间')),
                ('record_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backends.Item', verbose_name='浏览的商品')),
                ('record_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backends.User', verbose_name='隶属哪个用户')),
            ],
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('banner_id', models.AutoField(primary_key=True, serialize=False, verbose_name='轮播图')),
                ('banner_number', models.IntegerField(default=0, verbose_name='序号')),
                ('banner_image', stdimage.models.StdImageField(default='banner/image/itemDefault.jpg', upload_to='banner/image', verbose_name='轮播图')),
                ('banner_belong', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backends.Item', verbose_name='该轮播图属于哪个商品')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('address_id', models.AutoField(primary_key=True, serialize=False, verbose_name='收货地址')),
                ('address_username', models.CharField(max_length=100, verbose_name='姓名')),
                ('address_tel', models.CharField(max_length=20, verbose_name='联系方式')),
                ('address_detail', models.CharField(max_length=100, verbose_name='具体地址')),
                ('address_type', models.CharField(blank=True, max_length=10, null=True, verbose_name='地址类型')),
                ('address_isDefault', models.BooleanField(default=False, verbose_name='是否为默认地址')),
                ('address_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backends.User', verbose_name='隶属哪个用户')),
            ],
        ),
    ]