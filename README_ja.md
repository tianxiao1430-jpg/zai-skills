# ZAI-Skills

[English](./README.md) | [简体中文](./README_zh.md) | [日本語](./README_ja.md)

**Z.AI (Z Code)** プラットフォームとそのコア MCP エコシステム (Vision, Search, Zread) 専用に設計された、高性能な [Agent Skills](https://github.com/skillcreatorai/Ai-Agent-Skills) コレクションです。

## 🌟 なぜ ZAI-Skills なのか？

これらのスキルは、Z.AI インテリジェンス スイートの 3 つの主要な柱を強化するように最適化されており、高品質な技術出力のための高度な指示を提供します。

## 🚀 利用可能なスキル

| スキル | 説明 | トリガー |
|--------|------|----------|
| **`zai-orchestrator`** | 「頭脳」スキル。Vision、Search、Zread を連携させ、複雑で多段階のエンジニアリングタスクを解決します。 | 複雑タスク，多段階，協調，orchestrator |
| **`vision-expert`** | Z.AI Vision のための高度な UI-to-Code、技術図面分析、および視覚的なエラー診断。 | 画像分析，UI 変換，スクリーンショット診断，vision |
| **`search-expert`** | Z.AI Web Search Prime を使用した高精度な技術調査と構造化された情報の統合。 | 検索，調査，資料検索，search |
| **`zread-expert`** | Zread によるシニアアーキテクトレベルのコードベース分析、構造監査、およびセマンティック検索。 | リポジトリ分析，コード監査，zread, 設計分析 |

## 📖 使用例

### Vision Expert

| シナリオ | 入力例 | 期待される出力 |
|----------|--------|----------------|
| **UI 再現** | 「このデザインを React コンポーネントに変換して」+ [スクリーンショット] | 実行可能な React + Tailwind コード |
| **エラー診断** | 「このエラーを修正するには？」+ [ターミナルエラー画面] | ルート原因分析 + 具体的な修正コード |
| **図面分析** | 「このシステム設計を説明して」+ [設計図] | 設計内訳 + サービス/モジュール定義 |
| **OCR 抽出** | 「この画像からテキストを抽出して」+ [ドキュメント画像] | 構造化されたテキストコンテンツ |

**対話例：**
```
ユーザー：[UI スクリーンショットをアップロード] ログインページを実装して

アシスタント：このスクリーンショットを React + Tailwind コードに変換します。
           [ui_to_artifact を呼び出し]
           ✅ ログインコンポーネントを生成しました：
           - メール/パスワード入力フィールド
           - ローディング状態付きログインボタン
           - フォーム検証ロジック
           - レスポンシブデザイン
```

---

### Search Expert

| シナリオ | 入力例 | 期待される出力 |
|----------|--------|----------------|
| **技術調査** | 「Next.js と Remix の長所と短所を比較して」 | 構造化された比較 + 推奨事項 |
| **ベストプラクティス** | 「React パフォーマンス最適化のベストプラクティス」 | カテゴリ別最適化戦略 |
| **バージョン差異** | 「React 17 と比較して React 18 の新機能は」 | 新機能リスト + 移行ガイド |
| **エラー調査** | 「TypeError: Cannot read property of undefined の一般的な原因」 | 一般的な原因 + 解決策の概要 |

**対話例：**
```
ユーザー：2026 年のフロントエンド状態管理のトレンドを調査して

アシスタント：最新のフロントエンド状態管理ソリューションを検索しています...
           [zai-web-search を呼び出し]
           
📊 2026 フロントエンド状態管理トレンド：

## 主要ソリューション
1. **Zustand** - 軽量、中小規模プロジェクトに最適
2. **Jotai** - アトミック状態、きめ細かい更新に最適
3. **Redux Toolkit** - エンタープライズグレード、完全なエコシステム

## 新興トレンド
- サーバーコンポーネントによるクライアント状態の必要性減少
- Signals アプローチの台頭（SolidJS, Preact Signals）

## 推奨事項
- 小規模プロジェクト：Zustand
- 大規模プロジェクト：Redux Toolkit + サーバーコンポーネント
```

---

### Zread Expert

| シナリオ | 入力例 | 期待される出力 |
|----------|--------|----------------|
| **新規ライブラリ学習** | 「facebook/react のディレクトリ構造を分析して」 | プロジェクト構造 + コアモジュール紹介 |
| **ソースコード理解** | 「React の useEffect はどのように実装されていますか？」 | ソースパス + 実装ロジック |
| **Issue 調査** | 「このリポジトリの未解決の重大なバグは？」 | Issue リスト + 影響分析 |
| **コントリビューション準備** | 「このリポジトリにコントリビュートしたい、何を知っておくべき？」 | コントリビューションガイド + コード標準 |

**対話例：**
```
ユーザー：vercel/next.js のミドルウェアシステムがどのように機能するか分析して

アシスタント：Next.js ミドルウェアの実装を分析します...
           [zread.structure を呼び出し]
           [zread.search で"middleware"を検索]
           [zread.read でコアファイルを読み取り]
           
📦 Next.js ミドルウェアアーキテクチャ：

## コアファイル
- `packages/next/src/server/web/sandbox.ts` - サンドボックス環境
- `packages/next/src/server/web/spec-extension/` - Edge API
- `packages/next/middleware.ts` - ユーザーエントリーポイント

## 仕組み
1. Edge Runtime で実行
2. V8 Isolate を使用してユーザーコードを分離
3. spec-extension を通じて Next.js API を提供
```

---

### ZAI Orchestrator

| シナリオ | 入力例 | 使用するスキル | 期待される出力 |
|----------|--------|----------------|----------------|
| **フルスタック開発** | 「認証付きブログシステムを構築して」 | 全 4 スキル | 完全な設計 + コアコード |
| **複雑なバグ** | 「ローカルでは動作するが本番で失敗する」 | Orchestrator + Search + Zread | ルート原因 + 修正計画 |
| **技術選定** | 「リアルタイム共同編集エディタにはどのスタックを使うべき？」 | Orchestrator + Search | 技術比較 + 推奨事項 |
| **コード移行** | 「この jQuery プロジェクトを React に移行して」 | Orchestrator + Vision + Zread | 移行計画 + サンプルコード |

**対話例：**
```
ユーザー：Notion のようなオンラインドキュメントエディタを作りたい。どのように設計すべき？

アシスタント：<internal>
これは複数のスキルを必要とする複雑なタスクです：
1. Search - 既存ソリューションとベストプラクティスを調査
2. Zread - オープンソースの代替プロジェクト（AppFlowy など）を分析
3. Vision - 参考画像があれば UI レイアウトを分析

Triple-A ワークフローを開始します...
</internal>

オンラインドキュメントエディタの設計をサポートします。

## 📊 市場調査 (Search)
[調査結果：主流ソリューションには ProseMirror, TipTap, Slate.js など...]

## 📦 アーキテクチャ分析 (Zread)
[AppFlowy と同様のプロジェクトを分析：フロントエンドは React + TipTap、バックエンドは Rust...]

## 🏗️ 推奨技術スタック

### フロントエンド
- エディタコア：TipTap (ProseMirror ベース)
- フレームワーク：Next.js 14 (App Router)
- リアルタイムコラボレーション：Yjs + WebSocket

### バックエンド
- API：Next.js API Routes
- データベース：PostgreSQL + pgvector
- 同期サービス：PartyKit またはカスタム WebSocket

### デプロイ
- Vercel (フロントエンド) + Railway (バックエンド)

特定のモジュールを実装する必要がありますか？
```

---

## 🛠️ インストール方法

### 推奨：全スキルをインストール
```bash
# 4 つのスキルを一度にインストール
npx skills add https://github.com/tianxiao1430-jpg/zai-skills --all
```

### 個別インストール
```bash
# 特定のスキルをインストール
npx skills add https://github.com/tianxiao1430-jpg/zai-skills --skill vision-expert
npx skills add https://github.com/tianxiao1430-jpg/zai-skills --skill search-expert
npx skills add https://github.com/tianxiao1430-jpg/zai-skills --skill zread-expert
npx skills add https://github.com/tianxiao1430-jpg/zai-skills --skill zai-orchestrator
```

### スキルの依存関係

```
┌─────────────────────────────────────────┐
│         zai-orchestrator (脳)            │
│  Vision + Search + Zread を連携して       │
│  複雑なタスクを解決                      │
└─────────────┬───────────────────────────┘
              │ 依存
              ▼
    ┌─────────────────────────┐
    │                         │
    ▼                         ▼
┌──────────┐          ┌──────────────┐
│ vision   │          │ search       │
│ expert   │          │ expert       │
└──────────┘          └──────────────┘
       │                     │
       └──────────┬──────────┘
                  │
                  ▼
          ┌──────────────┐
          │ zread        │
          │ expert       │
          └──────────────┘
```

**注意：** `zai-orchestrator` を正常に機能させるには、3 つの expert スキルすべてをインストールする必要があります。

---

## 🔧 カスタマイズガイド

### スキルのカスタマイズ

各スキルは `SKILL.md` ファイルを編集してカスタマイズできます。一般的なカスタマイズ：

1. **ドメイン固有の知識を追加** - 業界に合わせてプロンプトを修正
2. **出力形式を調整** - レンステンプレートを変更
3. **例を追加** - 独自の使用例を含める

### スキルの組み合わせ

| タスクタイプ | 推奨組み合わせ |
|--------------|----------------|
| UI 変換 | vision-expert |
| 技術調査 | search-expert |
| コード分析 | zread-expert |
| 複雑なプロジェクト | **全 4 スキル** |
| フルスタック開発 | orchestrator + 全 expert |

---

## 📊 スキル比較

| 機能 | vision-expert | search-expert | zread-expert | orchestrator |
|------|---------------|---------------|--------------|--------------|
| **入力** | 画像/スクリーンショット | テキストクエリ | GitHub リポジトリ | あらゆる複雑タスク |
| **出力** | コード/診断 | 調査レポート | コード分析 | 包括的ソリューション |
| **用途** | UI 変換、OCR | 技術調査 | コードベース学習 | 多段階プロジェクト |
| **依存** | なし | なし | なし | 全 3 expert |

---

## 🤝 貢献する

これはコミュニティ主導のプロジェクトです！以下のような貢献を歓迎します：

1. **新しいスキルの提出** (Z.AI ツール向け)
2. **既存の指示の改善** による AI の信頼性向上
3. **事例の共有** - これらのスキルが問題を解決した実際の事例
4. **使用例の追加** - あなたの経験からの使用例

PR や Issue をお気軽にお送りください。最高の Z.AI ツールボックスを一緒に作り上げましょう！

### 開発ワークフロー

```bash
# 1. リポジトリをフォーク
git clone https://github.com/your-username/zai-skills

# 2. 新しいスキルを作成
cd zai-skills/skills
mkdir my-new-skill
# skill.json と SKILL.md を追加

# 3. ローカルでテスト
# AI エージェントで使用

# 4. PR を送信
git add .
git commit -m "feat: add my-new-skill"
git push origin main
```

---

## ❓ よくある質問

### Q: 4 つのスキルすべてが必要ですか？

**A:** 必ずしもありません。ニーズに応じて選択してください：
- **UI 作業のみ？** → vision-expert だけで十分
- **調査のみ？** → search-expert だけで十分
- **複雑なプロジェクト？** → 4 つすべてを推奨

### Q: Z.AI なしでこれらのスキルを使えますか？

**A:** これらのスキルは Z.AI MCP ツール（Vision, Search, Zread）専用に設計されています。これらのツールなしでは機能しません。

### Q: スキルをどのように更新しますか？

**A:** インストールコマンドを再実行してください：
```bash
npx skills update zai-skills
```

### Q: プロンプトをカスタマイズできますか？

**A:** はい！`SKILL.md` ファイルを編集して、独自の例やドメイン知識を追加できます。

---

## 📄 ライセンス

このプロジェクトは MIT ライセンスの下で公開されています。

## 🔗 関連プロジェクト

- [Z.AI MCP ツール](https://github.com/z-ai/mcp) - コア MCP ツール
- [Agent Skills 標準](https://github.com/skillcreatorai/Ai-Agent-Skills) - Skills 仕様
- [OpenClaw](https://github.com/openclaw/openclaw) - AI エージェントフレームワーク

---

**バージョン：** 1.0.0  
**最終更新日：** 2026-03-21  
**メンテナー：** [@tianxiao1430-jpg](https://github.com/tianxiao1430-jpg)
