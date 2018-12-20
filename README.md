# FinalReport2018
2018年の最終報告書管理用リポジトリです

# 注意事項
---
- ブランチ名は作業内容を書くこと
- 報告書の内容に関して変更を加える場合は,まずIssueを書き,assignすること
- Pull requestsを作成するときは自分の環境でコンパイルし、エラーが出ないことを確認すること
- push時にownerのレビューが必要であること
- レビュー方法
  - Pull requestからadd reviews
  - 問題なければapprove後マージ
---
# 構成
1. 概要
1. 目次
1. 研究背景
    1. ブラックジャックの戦略の歴史
    1. ブラックジャックのルール
        1. ゲームの流れ
        1. ディーラーの行動
    1. ブラックジャックにおける従来の戦略
        1. 従来の戦略
        1. ベーシックストラテジー
        1. ベーシックストラテジーの導出
        1. カウンティング
        1. ベッティングシステムの検討
1. プロジェクトの目標
    1. 前期における目標
    1. 後期における目標
1. 複雑性について
    1. 複雑性の定義
    1. 複雑性の検証実験
1. シミュレータについて
    1. 概要
    1. シミュレーションの条件設定
        1. デック数について
        1. デック数の違いによる影響
    1. ブラックジャックシミュレータ
    1. シミュレータの疑似乱数の検証
        1. 周期
        1. 等確立性の検定
1. ベーシックストラテジーの検証
    1. 戦略同士の比較
        1. ベーシックストラテジー改変1
        1. ベーシックストラテジー改変2
        1. プレイヤーの合計値が一定以上になるまでヒットする戦略
    1. 仮説
    1. 検証手順
    1. シミュレーション結果
    1. 検定
        1. カイ2乗検定による独立性の検定
        1. 残差分析
        1. 多重比較
    1. 複雑性を考慮した性能比較とその結果
        1. 各戦略の複雑性
        1. 各戦略の性能評価
    1. 検証結果のまとめ
1. 遺伝的アルゴリズムを用いた戦略の探索
    1. 遺伝的アルゴリズム
        1. 概要
        2. アルゴリズムの説明
        3. 遺伝子コーディング
        4. 選択アルゴリズム
        5. 交叉アルゴリズム
        6. 突然変異アルゴリズム
        7. 実験条件
        8. 実験結果
        9. GA戦略の戦績
1. 一定ベットのシミュレーション
1. カウンティングを用いたシミュレーション
1. 検証結果
    1. 賭け金の導入
        1. 使用する戦略について
        1. 一定ベット
            1.戦略の紹介
        1. 勝率推移
        1. カウンティング
        1. エラー率
            1. 分散分析
            1. 多重比較
1. 前期活動
1. 後期活動
1. 中間発表の評価
    1. 評価点数の集計
    1. コメント解析と改善点
1. 最終発表の評価
    1. 評価点数の集計
    1. コメント解析と改善点
1. 今後の課題
1. 参考/引用文献
1. 付録
