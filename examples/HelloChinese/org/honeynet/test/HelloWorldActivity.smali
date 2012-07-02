.class public Lorg/honeynet/test/HelloWorldActivity;
.super Landroid/app/Activity;
.source "HelloWorldActivity.java"


# instance fields
.field private mTextView:Landroid/widget/TextView;


# direct methods
.method public constructor <init>()V
    .registers 1

    invoke-direct {p0}, Landroid/app/Activity;-><init>()V

    return-void
.end method


# virtual methods
.method public onCreate(Landroid/os/Bundle;)V
    .registers 5

    invoke-super {p0, p1}, Landroid/app/Activity;->onCreate(Landroid/os/Bundle;)V

    const/high16 v1, 0x7f03

    invoke-virtual {p0, v1}, Lorg/honeynet/test/HelloWorldActivity;->setContentView(I)V

    const/high16 v1, 0x7f05

    invoke-virtual {p0, v1}, Lorg/honeynet/test/HelloWorldActivity;->findViewById(I)Landroid/view/View;

    move-result-object v1

    check-cast v1, Landroid/widget/TextView;

    iput-object v1, p0, Lorg/honeynet/test/HelloWorldActivity;->mTextView:Landroid/widget/TextView;

    iget-object v1, p0, Lorg/honeynet/test/HelloWorldActivity;->mTextView:Landroid/widget/TextView;

    const-string v2, "\u6b22\u8fce\u6765\u5230APKIL\u7684\u4e16\u754c"

    invoke-virtual {v1, v2}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V

    :try_start_19
    iget-object v1, p0, Lorg/honeynet/test/HelloWorldActivity;->mTextView:Landroid/widget/TextView;

    const-string v2, "APKIL\u662f\u4e00\u4e2aAPK\u63d2\u6869\u5e93"

    invoke-virtual {v1, v2}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V
    :try_end_20
    .catch Ljava/lang/Exception; {:try_start_19 .. :try_end_20} :catch_21

    :goto_20
    return-void

    :catch_21
    move-exception v0

    invoke-virtual {v0}, Ljava/lang/Exception;->printStackTrace()V

    goto :goto_20
.end method
